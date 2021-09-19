# 静态资源类

class JavaAnnotation:
    head = '/**'
    params = []
    tail = '*/'
    lineSplit = '* '
    author = '@author 作者 sean'
    version = '@version 版本号 1.0.0@snapshot'
    functionNameDec = '[] 方法名'
    paramsDec = '@params 参数 '
    className = '* className '
    functionName = ''
    description = ''
    singleLine = '//'

    def __init__(self, params):
        self.params = params

    def __str__(self):
        volume = []
        for i in self.params:
            volume.append('/* '+i+'\n')
        result = self.head + ''.join(volume) + self.tail
        return result



