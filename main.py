from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import webbrowser


kv = """
#:import Snackbar kivymd.uix.snackbar.Snackbar
#:import Clipboard kivy.core.clipboard.Clipboard

Screen:

    NavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout :
                    orientation : 'vertical'

                    MDToolbar:
                        title : 'HomeWork'
                        md_bg_color: .2, .2, .2, 1
                        specific_text_color: 1, 1, 1, 1
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation : 9
                        Widget:


                    MDBottomNavigation:

                        MDBottomNavigationItem:
                            name : 'S1'
                            text : 'Info'
                            icon : 'information'    

                            ScrollView:
                                MDList:
                                    ThreeLineAvatarListItem:
                                        text: "ASSIGNMENTS"
                                        secondary_text: "Click here for rates"
                                        tertiary_text : "100% Reasonable"

                                        on_release : app.reward()

                                        ImageLeftWidget:
                                            source: "download.jpg"

                                    ThreeLineAvatarListItem:
                                        text: "PRACTICALS"
                                        secondary_text: "Click here for rates"
                                        tertiary_text : "100% Reasonable"
                                        on_release : app.reward()

                                        ImageLeftWidget:
                                            source: "CBSE-12th-Chemistry-Notes-All-Chapters.jpg"

                                    ThreeLineAvatarListItem:
                                        text : 'PROJECTS'
                                        secondary_text: "Click here for rates"
                                        tertiary_text : "100% Reasonable"
                                        on_release : app.reward()

                                        ImageLeftWidget :
                                            source : "download (1).jpg"

                                    ThreeLineAvatarListItem:
                                        text: "CC"
                                        secondary_text: "Click here for rates"
                                        tertiary_text : "100% Reasonable"
                                        on_release : app.reward()

                                        ImageLeftWidget:
                                            source: "download.jpg"
                                    
                                    ThreeLineAvatarListItem:
                                        text : 'NOTES/IMP'
                                        secondary_text: "All schools/universities"
                                        tertiary_text : "Free of cost"
                                        on_release : app.show()

                                        ImageLeftWidget :
                                            source : "download (2).jpg"           

                                    ThreeLineAvatarListItem:
                                        text : 'PREVIOUS QUESTION PAPERS'
                                        secondary_text: "All school/universities"
                                        tertiary_text : "Free of cost"
                                        on_release : app.show()

                                        ImageLeftWidget :
                                            source : "download (3).jpg"           



                        MDBottomNavigationItem:
                            name : 'S3'
                            text : 'Work'
                            icon : 'lightbulb'    

                            MDLabel:
                                text: 'Send Us Details(Fill Form)'
                                font_style : 'Subtitle1'
                                theme_text_color : 'Primary'  
                                pos_hint:{'x':0.20,'y':0.45}

                            MDTextField:
                                hint_text: "Enter Contact Number"
                                max_text_length : 10
                                helper_text_mode: "on_focus"
                                pos_hint : {'x':0.03,'y':0.75}

                            MDTextField:
                                hint_text: "Do you Provide helping material"
                                helper_text: "Enter Yes or No"
                                helper_text_mode: "on_focus" 
                                pos_hint : {'x':0.03,'y':0.60}

                            MDTextField:
                                hint_text: "You want your work in less than 24 hours"
                                helper_text: "Enter Yes or No"
                                helper_text_mode: "on_focus"    
                                pos_hint : {'x':0.03,'y':0.45}

                            MDTextField:
                                hint_text: "Enter Deadline"
                                helper_text: "Date you want for your work to be complete"
                                helper_text_mode: "on_focus"   
                                pos_hint : {'x':0.03,'y':0.30}

                            MDFillRoundFlatButton:
                                text : "Click Here"
                                pos_hint:{'x':0.35,'y':0.20}              
                                size_hint:0.25,0.08
                                on_release: 
                                    Snackbar(text="Take ScreenShot!").show()   
                                    
                            MDFillRoundFlatButton:
                                text : "Contact"
                                pos_hint:{'x':0.35,'y':0.10}
                                size_hint:0.25,0.08
                                on_release:
                                    app.Contact()

                        MDBottomNavigationItem:
                            name : 'S4'
                            text : 'Notes'
                            icon : 'notebook'    

                            MDLabel:
                                text: 'Free Notes/IMP(Fill Form)'
                                font_style : 'Subtitle1'
                                theme_text_color : 'Primary'  
                                pos_hint:{'x':0.20,'y':0.45}

                            MDTextField:
                                hint_text: "Name Institute"
                                helper_text: "School/University"
                                multiline : True 
                                helper_text_mode: "on_focus"
                                pos_hint : {'x':0,'y':0.75}


                            MDTextField:
                                hint_text: "Class/Semester"
                                helper_text_mode: "on_focus"   
                                pos_hint : {'x':0,'y':0.60}

                            MDTextField:
                                hint_text: "Subject/Topic"
                                helper_text_mode: "on_focus" 
                                pos_hint : {'x':0,'y':0.45}

                            MDTextField:
                                hint_text: "Your Contact Number "
                                helper_text_mode: "on_focus"    
                                pos_hint : {'x':0,'y':0.30}

                            
                            MDFillRoundFlatButton:
                                text : "Click Here"
                                pos_hint:{'x':0.35,'y':0.20}              
                                size_hint:0.25,0.08
                                on_release: 
                                    Snackbar(text="Take ScreenShot!").show()   
                                    
                            MDFillRoundFlatButton:
                                text : "Contact"
                                pos_hint:{'x':0.35,'y':0.10}
                                size_hint:0.25,0.08
                                on_release:
                                    app.Contact()   
                            
        MDNavigationDrawer:
            id : nav_drawer                              
            BoxLayout:
                orientation : 'vertical'
                padding : '8dp'
                spacing : '8dp'

                Image:
                    source:'3.jpg'

                MDLabel:
                    text: "MIH-CREATION(CONTACT-US)"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: "rikkisha49@gmail.com"
                    size_hint_y: None
                    font_style: "Caption"
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineAvatarListItem:
                            text: "Facebook"
                            pos_hint : {'x':0,'y':0.5}
                            on_press : app.facebook()

                            ImageLeftWidget:
                                source: "download (4).jpg"

                        OneLineAvatarListItem:
                            text: "Instagram"
                            on_press : app.instagram()

                            ImageLeftWidget:
                                source: "download (5).jpg"


                        OneLineAvatarListItem:
                            text: "WhatsApp"
                            on_release:
                                text = Clipboard.paste()
                                Clipboard.copy('7000567551')
                                Snackbar(text="WhatsApp Number copied!").show()

                            ImageLeftWidget:
                                source: "download (6).jpg"


"""


class mainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.data_tables = MDDataTable(
            size_hint=(0.8, 0.5),
            column_data=[
                ("Work", dp(45)),
                ("Cost", dp(45)),
                ("Time", dp(45)),
            ],
            row_data=[
                # The number of elements must match the length
                # of the `column_data` list.
                ("Assignment", "3Rs/Page(2 sides) + Material", "24 hours"),
                ("Project", "cost of Project + Our Charge", "Depends on Project"),
                ("Practical", "3Rs/Page(2 sides) + Material ", "24 hours"),
                ("Fast Service", "5Rs/Page(2 sides) + Material ", "less than 24 hours"),
            ]
        )

        return Builder.load_string(kv)

    def reward(self):
        self.data_tables.open()

    def show(self):
        self.dialog = MDDialog(
            title='How to Connect?',
            text="Connect With Us Following These Steps \n1) Fill Notes form! \n2) Take ScreenShot \n3) Click On Top-left-corner Icon. \n4)Send ScreenShot On Any Given Platform. ",
            size_hint=(0.7, 0.5),
            buttons=[
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color, on_press=self.dismiss
                ),
                MDFlatButton(
                    text="Done", text_color=self.theme_cls.primary_color, on_press=self.dismiss
                ),
            ],
        )

        self.dialog.open()

    def Contact(self):
        self.dialog = MDDialog(
            title='How to Connect?',
            text="Connect With Us Following These Steps \n1) Fill Notes form! \n2) Take ScreenShot \n3) Click On Top-left-corner Icon. \n4)Send ScreenShot On Any Given Platform. ",
            size_hint=(0.8, 0.6),
            buttons=[
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color, on_press=self.dismiss
                ),
                MDFlatButton(
                    text="Done", text_color=self.theme_cls.primary_color, on_press=self.dismiss
                ),
            ],
        )

        self.dialog.open()


    def dismiss(self, obj):
        self.dialog.dismiss()


    def facebook(self):
        self.web = webbrowser.open("https://www.facebook.com/Home-Work-106918057844725/")

    def instagram(self):
        self.ins = webbrowser.open(
            "https://www.instagram.com/homework_assign/?igshid=levzzeoh0rrt&fbclid=IwAR3huKGtL99qynenJJiv9iF6CbKHfCDnSZdCarBJHlZykfNjESgVbUTkCgo")


mainApp().run()
