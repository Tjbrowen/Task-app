from flet import *

def main(page: Page):
   BG = '#041955'
   FWG = '#97B4ff'
   FG = '#3450A1'
   PINK ='#eb06ff'

   content=categories_card = Row(
      
   )
   categories = ['Business','Family', 'Friends']
   for category in categories:
      categories_card.controls

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
            )
         ]
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

app(target=main)

