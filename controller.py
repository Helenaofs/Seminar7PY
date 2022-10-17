import imprt
import export
import view
import logger

def start():
    if view.mod() == '1':
        info = view.exp()
        export.my_export(info)
        logger.log_info(info)
    else:
        info = view.inp()
        imprt.imp(info)
        logger.log_info(info)
