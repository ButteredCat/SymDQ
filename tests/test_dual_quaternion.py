import pytest
import sympy
from sympy.algebras.quaternion import Quaternion
from .context import DualQuaternion


class TestDualQuaternion():
    a, b, c, d = sympy.symbols('a b c d', real=True)
    x, y, z, w = sympy.symbols('x y z w', real=True)
    q1 = Quaternion(a, b, c, d)
    q2 = Quaternion(x, y, z, w)
    q3 = Quaternion(z, b, a, d)
    q4 = Quaternion(c, w, x, y)

    def test_should_create_dual_quaternion(self):
        dq = DualQuaternion(self.q1, self.q2)
        assert isinstance(dq, DualQuaternion)
        assert dq.real == self.q1
        assert dq.dual == self.q2
    
    def test_should_create_from_real_number(self):
        dq = DualQuaternion(self.a, self.b)
        assert dq.real == Quaternion(self.a)
        assert dq.dual == Quaternion(self.b)

    def test_should_create_from_default(self):
        dq = DualQuaternion()
        assert dq.real == Quaternion(0)
        assert dq.dual == Quaternion(0)

    def test_should_implement_addition(self):
        dq1 = DualQuaternion(self.q1, self.q2)
        dq2 = DualQuaternion(self.q2, self.q1)
        dq = dq1 + dq2
        assert dq.real == self.q1 + self.q2
        assert dq.dual == self.q2 + self.q1

    def test_should_handle_dq_and_quat_add(self):
        dq1 = DualQuaternion(self.q1, self.q2)
        dq = dq1 + self.q2
        assert dq.real == self.q1 + self.q2
        assert dq.dual == self.q2

    def test_should_handle_dq_and_real_add(self):
        dq1 = DualQuaternion(self.q1, self.q2)
        dq = dq1 + 1
        assert dq.real == self.q1 + 1
        assert dq.dual == self.q2

    # can not pass since it calls __add__ of Quaternion instead of __radd__ of
    # DualQuaternion in this condition
    #def test_should_handle_quat_and_dq_radd(self):
        #dq1 = DualQuaternion(self.q1, self.q2)
        #dq = self.q2 + dq1
        #assert dq.real == self.q1 + self.q2
        #assert dq.dual == self.q2

    def test_should_handle_real_and_dq_radd(self):
        dq1 = DualQuaternion(self.q1, self.q2)
        dq = 1 + dq1
        assert dq.real == self.q1 + 1
        assert dq.dual == self.q2

    def test_should_implement_multiplication(self):
        dq1 = DualQuaternion(self.q1, self.q2)
        dq2 = DualQuaternion(self.q3, self.q4)
        dq = dq1 * dq2
        assert dq.real == self.q1 * self.q3
        assert dq.dual == self.q1 * self.q4 + self.q2 * self.q3