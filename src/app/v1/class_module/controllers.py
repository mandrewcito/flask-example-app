class SubBluePrint(object)
    def __init__(self,module_name,name,url_prefix):
        self.module_name = module_name
        self.__name__ = name
        self.url_prefix = url_prefix


class ClassModule(SubBluePrint):
    def __init__(self):
        super(ClassModule,self).__init__("class_module",__name__,url_prefix='/class_module')

    def hello(self):
        return "hello,world"
