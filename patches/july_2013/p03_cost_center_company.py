import webnotes

def execute():
	webnotes.reload_doc("accounts", "doctype", "cost_center")
	webnotes.conn.sql("""update `tabCost Center` set company=company_name""")
	webnotes.conn.sql_ddl("""alter table `tabCost Center` drop column company_name""")