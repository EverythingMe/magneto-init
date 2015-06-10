# coding=utf-8
from magneto.base import BaseTestCase
from magneto.utils.assertion import Assert


class TestExample(BaseTestCase):
    """
    This is the test suite name
    """

    def test_1(self):
        """
        Test example 1
        """

        # click button
        button = self.magneto(text='Click me')
        button.click()

        # scroll list to bottom
        list = self.magneto(className='android.widget.ListView')
        list.fling.toEnd()

        # make sure last item exists
        last_item = self.magneto(text="last item")
        Assert.true(last_item.exists)
