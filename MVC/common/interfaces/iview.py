class IView(object):

    def setController(self, controller):
        raise (NotImplementedError)

    def run(self):
        raise NotImplementedError("Not yet implemented")