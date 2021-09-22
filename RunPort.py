# 执行脚本的入口
import JavaAnnotation
import OptionDocx
from translate import Translator
from docx import Document
import re



if __name__ == '__main__':
    # option = OptionDocx
    # option.handDocs()

    # testList = 'public class Context'
    #
    # if ' ' in testList:
    #     str = testList[int(testList.rfind(' ')) + 1:len(testList)]
    #     print(str)
    #     translator = Translator("chinese")
    #     translation = translator.translate('Context')
    #     print(translation)
    # javaAnnotation = '* description '
    # #staticStr = '用户选择发生额及金额查询条件功能，进入发生额及金额查询条件界面。在此界面中用户可以看到发生额及金额查询的各种条件，如月份，科目，级数，科目类型以及其他相关信息。同时可以进行增加，保存、删除等功能操作。详情如下图所示。'
    # staticStr = '用户选择发生额及金额查询条件'
    # for i in handDesc(staticStr):
    #     print('line:' + i + '\n')
    # print('hello')
    #
    # functionList = []
    # classList = []
    # path = "/Users/sean/Downloads/2会计总帐专业版智能管理系统/1  java  2会计总帐专业版智能管理系统.docx"
    #
    # infoDocument = Document(path)
    # docLen = len(infoDocument.paragraphs)
    # pageLine = 48
    # totalPage = docLen / 48
    # print('totalPage %d'% totalPage)
    pass
    option = OptionDocx
    option.handDocs('', '')
    # option.handDocs('', '')
    # straa = 'public class ALAAgentPromRadixBLS{'
    # asada = 'public Command getCommand   ()'
    # sa = asada.split(' ')
    # # print(sa)
    # print(option.extractFunctionName(asada, ' '))


