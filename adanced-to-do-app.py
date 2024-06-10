from flet import *

def main(page: Page):
   BG = '#041955'
   FWG = '#97B4ff'
   FG = '#3450A1'
   PINK ='#eb06ff'

   def route_change(route):
      page.views.clear()
      page.views.append(
         View(
            "/",
            [
               container
            ],
         ),
      )

   tasks = Column()

   content=categories_card = Row(
      scroll='auto'
      

   )
   categories = ['Business','Family', 'Friends']
   for i, category in enumerate (categories):
      categories_card.controls.append(
         Container(
            border_radius=20,
            bgcolor=BG,
            width=170,
            height=110,
            padding=15,
            content=Column(
               controls=[
                  Text('40 Tasks', color='white'),
                  Text(category, color='white'),
                 Container(
                    width=160,
                    height=5,
                    bgcolor='white12',
                    border_radius=20,
                    padding=padding.only(right=i*30),
                    content=Container(
                       bgcolor=PINK,
                    )
                 )
               ]
            )
            
      )
      )
   first_page_contents = Container(
      content=Column(
         controls=[
            Row(
               alignment=MainAxisAlignment.SPACE_BETWEEN,
               controls=[
                  Container(
                     content=Icon(
                        icons.MENU,
                        color='white'  # Set the icon color to white
                     )
                  ),
                  Row(
                     controls=[
                        Icon(icons.SEARCH, color='white'),
                        Icon(icons.NOTIFICATIONS_OUTLINED, color='white')
                     ]
                  )
               ]
            ),
            Container(height=20),
            Text(
               value="What's up, Jimmy!",
               color='white'  # Optionally, set the text color to white
            ),
            Text(
               value='CATEGORIES',
               color='white'
            ),
            Container(
               padding=padding.only(top=10,bottom=20,),
               content=categories_card
            ),
            Container(height=20),
            Text("TODAY'S TASKS", color='white'),
            Stack(
               controls=[
                  tasks,
                  FloatingActionButton(
                     icon = icons.ADD,on_click=lambda _: page.go
                     ('/create_task')
                  )
               ]
            )
         ],
      )
    )

   page_1 = Container()
   page_2 = Row(
      controls=[
         Container(
            width=400,
            height=850,
            bgcolor=FG,
            border_radius=35,
            padding=padding.only(
               top=50,
               left=20,
               right=20,
               bottom=5
            ),
            content=Column(
               controls=[
                  first_page_contents
               ]
            )
         )
      ]
   )

   container = Container(
      width=400,
      height=850,
      bgcolor=BG,
      border_radius=35,
      content=Stack(
         controls=[
            page_1,
            page_2,
         ]
      )
   )
   page.add(container)
   
   page.on_route_change = route_change
   page.go(page.route)


app(target=main)

