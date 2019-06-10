class embedstats:
    def __init__(self, choice):
        if(choice == 0):
            self.title = "Joseph Stalin"
            self.health = 64625
            self.offense = 52795
            self.defense = 57953
            self.field_effect_1_title = "AntiCapitalist"
            self.field_effect_1_desc = "'Capitalist' Class enemies' Offense and Defense -90%; 'Communist' Class allies' damage doubled against 'Capitalist' Class enemies"
            self.field_effect_2_title = "Disappearing Act"
            self.field_effect_2_desc = "Defeated 'Capitalist' Class enemies are permanently removed from battle"
            self.classes = "Communist; Supreme Leader; Dictator"
            self.footer = "The OG supreme communist ruler."
        elif(choice == 1):
            self.title = "Kim Jong-Un"
            self.health = 42685
            self.offense = 37894
            self.defense = 22685
            self.field_effect_1_title = "Supreme Leader"
            self.field_effect_1_desc = "'Communist' Class enemies obey Kim Jong-Un; 'Supreme Leader' and 'Dictator' Class enemies are unaffected"
            self.field_effect_2_title = "Self-Confidence"
            self.field_effect_2_desc = "If Kim Jong-Un defeats a 'Capitalist' Class enemy, he recovers 25% Health lost"
            self.classes = "Communist; Supreme Leader; Dictator"
            self.footer = "All hail."
        elif(choice == 2):
            self.title = "General Drumpf"
            self.health = 14673
            self.offense = 52798
            self.defense = 94363
            self.field_effect_1_title = "Murica"
            self.field_effect_1_desc = "'Capitalist' Class allies' Offense +25%"
            self.field_effect_2_title = "It's Just Capitalism"
            self.field_effect_2_desc = "When HP is below 50%, Offense +5000 and 'Capitalist' Class allies' Offense and Defense -30%"
            self.classes = "Capitalist; Supreme Leader; Dictator"
            self.footer = "Making Murica degenerate again."
        elif(choice == 3):
            self.title = "Uncle Sam"
            self.health = 63157
            self.offense = 36798
            self.defense = 75736
            self.field_effect_1_title = "Stars and Stripes"
            self.field_effect_1_desc = "'Capitalist' Class allies ignore 'Communist' Class enemies' Offense increases"
            self.field_effect_2_title = "Lighting the Fuse"
            self.field_effect_2_desc = "Offense +100% when there are no allies remaining"
            self.classes = "Capitalist"
            self.footer = "Stars, stripes, and fireworks. 'Murica."
        elif(choice == 4):
            self.title = "Moon Lord"
            self.health = 90426
            self.offense = 84783
            self.defense = 36734
            self.field_effect_1_title = "Celestial Entity"
            self.field_effect_1_desc = "Ignores enemies' Defense increases"
            self.field_effect_2_title = "Moon Leech Clots"
            self.field_effect_2_desc = "Health recovered by 500 whenever an enemy is attacked"
            self.classes = "God; Video Game"
            self.footer = "Impending doom approaches."
        elif(choice == 5):
            self.title = "Wood Man"
            self.health = 78353
            self.offense = 35784
            self.defense = 62136
            self.field_effect_1_title = "Robotic Armor"
            self.field_effect_1_desc = "Ignores enemies' Offense increases"
            self.field_effect_2_title = "Leaf Shield"
            self.field_effect_2_desc = "Enemies attacking Wood Man receive 500 damage"
            self.classes = "Video Game"
            self.footer = "doot doot doot."
        elif(choice == 6):
            self.title = "Shulk"
            self.health = 41313
            self.offense = 67834
            self.defense = 53323
            self.field_effect_1_title = "Monado Arts"
            self.field_effect_1_desc = "Offense +25% after receiving attack; only activates once"
            self.field_effect_2_title = "Back Slash"
            self.field_effect_2_desc = "Unleashes a wicked Back Slash when attacking, ignoring enemies' Defense increases and dealing +5000 damage to 'Video Game' Class enemies"
            self.classes = "Seems Familiar; Video Game"
            self.footer = "He's really feeling it."
        elif(choice == 7):
            self.title = "Copper Comrade"
            self.health = 44462
            self.offense = 45734
            self.defense = 101835
            self.field_effect_1_title = "Go Forth, Comrades!"
            self.field_effect_1_desc = "'Communist' Class allies' Offense +50%"
            self.field_effect_2_title = "Overwhelming Copper Defenses"
            self.field_effect_2_desc = "Ignores the Field Effects of 'Capitalist' Class enemies"
            self.classes = "Communist; Chastiser"
            self.footer = "Red and yellow make brown, and copper is brown. Therefore, Copper COmrade is yellow and red."