def singleton(aClass):
    def onCall(*args, **kwargs):
        if onCall.instance is None:
            onCall.instance = aClass(*args, **kwargs)
        return onCall.instance
    onCall.instance = None
    return onCall
