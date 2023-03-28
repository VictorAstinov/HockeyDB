from flask import Blueprint, request
from model.Team import Team, search_teams, search_teams_played
from errors import basic_exception_handler


bp = Blueprint('team', __name__)


# GET http://127.0.0.1/api/players?name=<name>
# GET http://127.0.0.1/api/players?player_ids=<player1>,<player2>
@bp.route('/', methods=['GET'], strict_slashes=False)
@basic_exception_handler
def get_teams():
    args = request.args
    team_name = args.get("name")
    players = []

    if 'team_ids' in args:
        players = args.get('team_ids').split(",")

    teams = search_teams(
        team_name=team_name,
        players=players,
    )
    return {'teams': [team.to_dict() for team in teams]}


@bp.route('/', methods=['POST'], strict_slashes=False)
@basic_exception_handler
def create_team():
    body = request.get_json()
    abbrv = body.get('abbrv')
    team_name = body.get('team_name')
    logo_url = body.get('logo_url')
    since = body.get('since')
    location = body.get('location')

    team = Team(
        abbrv=abbrv,
        team_name=team_name,
        logo_url=logo_url,
        since=since,
        location=location,
    )
    team.create()
    return {'status': 'OK', 'team_id': team.team_id}


@bp.route('/<team_id>', methods=['GET'])
@basic_exception_handler
def get_team(team_id: int):
    team = Team(team_id=team_id)
    team.get()
    return team.to_dict()


# TODO merge with GET /
@bp.route('/played', methods=['GET'])
@basic_exception_handler
def get_played_teams():
    player_id = request.args.get("player_id", default=None, type=str)
    teams = search_teams_played(
        player_id=player_id,
        fuzzy=True
    )
    return {'teams': [team.to_dict() for team in teams]}


@bp.route('/<team_id>', methods=['PATCH'])
@basic_exception_handler
def modify_team(team_id: int):
    team = Team(team_id=team_id)
    team.get()

    body = request.get_json()
    team.abbrv = body.get('abbrv')
    team.team_name = body.get('team_name')
    team.logo_url = body.get('logo_url')
    team.since = body.get('since')
    team.location = body.get('location')

    team.update()
    return {'status': 'OK'}


@bp.route('/<team_id>', methods=['DELETE'])
@basic_exception_handler
def delete_team(team_id: int):
    team = Team(team_id=team_id)
    team.delete()

    return {'status': 'OK'}


# @bp.route('/<team_id>/timeline', methods=['GET'])
# @basic_exception_handler
# def get_team_history(team_id: int):
#     # TODO
#     pass


# @bp.route('/<team_id>/timeline', methods=['DELETE'])
# @basic_exception_handler
# def modify_team_history(team_id: int):
#     # TODO
#     pass
