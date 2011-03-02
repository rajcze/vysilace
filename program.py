import MVC.common.interfaces
import MVC.controller
import MVC.model.pydata
import MVC.view.qt


if __name__ == "__main__":
    model = MVC.model.pydata.PyDataModel()
    view = MVC.view.qt.QtView()
    controller = MVC.controller.Controller(model, view)

    view.run()
