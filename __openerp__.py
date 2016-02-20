# _*_ coding: utf-8 _*_
{
    'name': "account_voucher_journal_filter",
    'version': '1.0',
    'depends': ["account", "account_voucher"],
    'author': "糖葫芦(39181819@qq.com)",
    'category': '',
    'data': ["views/account_journal_view.xml",
             "views/account_voucher_view.xml",
             "security/ir.model.access.csv"],
    'demo': [],
    'description': """
    在invoice登记付款向导、客户付款、供应商付款这三个界面上，增加对journal分组选择的功能

    2016-2-15 更新内容

    1 没有选择一个group的时候，journal选择框是隐藏的

    2 选择了一个group，journal默认选择符合当前筛选条件的第一个journal
    """,
}
