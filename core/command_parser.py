from logging import getLogger


log = getLogger(__name__)


def parse_cmd(cmd:str):
    if not cmd:
        log.error('Command required')
        return None, None
    tokens = cmd.split()
    command = tokens[0]
    params = ','.join(tokens[1:])
    params = params.split(',') if params else []
    return command, params


def parse_place_params(x, y, f:str):
    kwargs = {'x': int(x), 'y': int(y), 'f': f}
    return kwargs
