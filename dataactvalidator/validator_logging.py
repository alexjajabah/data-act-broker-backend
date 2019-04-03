from os import getpid, getppid

import psutil
from flask import current_app, g, _app_ctx_stack

from dataactcore.interfaces.db import GlobalDB


# ============================================================
# DIAGNOSTIC CODE
# - to to be used while under test, then removed
# ============================================================
def log_session_size(logger, job_id=None, checkpoint_name='<unspecified>'):
    message = "Diagnostic on SQLAlchemy Session object [{}] at [{}]".format(
        GlobalDB.db().session,
        checkpoint_name,
    )
    log_metadata_dict = {'memory': dict(psutil.Process().memory_full_info()._asdict())}
    log_job_message(logger, message, job_id, is_debug=True, other_params=log_metadata_dict)
# ============================================================


def log_job_message(logger, message, job_id=None,
                    is_debug=False, is_warning=False, is_error=False, is_exception=False,
                    other_params={}):
    """Handles logging a message about a validator job, with additional job metadata"""
    log_dict = {
        'proc_id': getpid(),
        'parent_proc_id': getppid(),
        'job_id': job_id,
        'current_app': hex(id(current_app)) if current_app else None,
        'flask.g': hex(id(g)) if g else None,
        '_app_ctx_stack.__ident_func__': hex(_app_ctx_stack.__ident_func__()) if _app_ctx_stack else None,
        'db_session': hex(id(GlobalDB.db().session)),
        'message': message,
        'message_type': 'BrokerValidator'
    }

    for param in other_params:
        if param not in log_dict:
            log_dict[param] = other_params[param]

    if is_exception:  # use this when handling an exception to include exception details in log output
        logger.exception(log_dict)
    elif is_error:
        logger.error(log_dict)
    elif is_warning:
        logger.warning(log_dict)
    elif is_debug:
        logger.debug(log_dict)
    else:
        logger.info(log_dict)