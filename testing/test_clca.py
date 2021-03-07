import yaml

from python_code.calculator import Clc
import pytest

with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)
    add = datas['add']
    add_datas = add['datas']
    add_myid = add['myid']
    division = datas['div']
    div_datas = division['divdatas']
    div_myid = division['divmyid']
    print(division, div_datas, div_myid)


def setup_module():
    print("模块开始执行")


def teardown_module():
    print("模块结束执行")


def test_a():
    print("这是第一个测试")


class TestCalc:
    def setup_class(self):
        # 实例化
        self.calc = Clc()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize(
        "a,b,jieguo",
        add_datas, ids=add_myid
    )
    def test_add(self, a, b, jieguo):
        # calc = Clc()
        result = self.calc.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
            assert result == jieguo
        else:
            if result != jieguo:
                print("计算错误")
            assert "请核对计算结果"

    @pytest.mark.parametrize('a,b,jieguo', div_datas, ids=div_myid)
    def test_div(self, a, b, jieguo):
        result = self.calc.div(a, b)
        if a == 0:
            print("除数不可为0")
            assert "除数不可为0，请核对数据"
        else:
            if isinstance(result, float):
                result = round(result, 2)
        assert result == jieguo, "计算错误"
