{
   'name'        : "Academy",
   'summary'     : """ERW Academy Module""",
   'description' : """Custom Module for manage Course in Academy""",
   'author'      : "Erwin Mapaliey",
   'website'     : "https://github.com/erwinmapaliey",
   'category'    : 'Uncategorized',
   'version'     : '0.1',
   'depends'     : ['base'],
   
   'data': [
      'security/ir.model.access.csv',
      'views/academy_menuitem.xml',
      'views/academy_course_view.xml',
   ],
}
