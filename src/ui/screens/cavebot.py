import kivy.context
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.selectioncontrol.selectioncontrol import MDCheckbox
from kivymd.uix.screen import MDScreen


class CavebotScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selectedDirection = 'north'
        self.waypoints = []
        wrapperLayout = MDBoxLayout()
        anchorLayout = AnchorLayout()
        self.data_tables = MDDataTable(
            use_pagination=False,
            check=False,
            column_data=[
                ('Label', dp(15)),
                ('Tipo', dp(15)),
                ('X', dp(15)),
                ('Y', dp(15)),
                ('Z', dp(15)),
                ('Opções', dp(15)),
            ],
            row_data=[
            ],
            sorted_on='ID',
            sorted_order='ASC',
            elevation=0,
        )
        self.data_tables.bind(on_row_press=self.on_row_press)
        anchorLayout.add_widget(self.data_tables)
        buttonsLayout = MDBoxLayout(orientation='vertical')

        westCheckbox = MDCheckbox(group='direction')
        westCheckbox.bind(active=lambda _, checked: self.onCheckDirection('west', checked))
        eastCheckbox = MDCheckbox(group='direction')
        eastCheckbox.bind(active=lambda _, checked: self.onCheckDirection('east', checked))
        northCheckbox = MDCheckbox(active=True, group='direction')
        northCheckbox.bind(active=lambda _, checked: self.onCheckDirection('north', checked))
        southCheckbox = MDCheckbox(group='direction')
        southCheckbox.bind(active=lambda _, checked: self.onCheckDirection('south', checked))
        buttonsLayout.add_widget(northCheckbox)
        buttonsLayout.add_widget(westCheckbox)
        buttonsLayout.add_widget(eastCheckbox)
        buttonsLayout.add_widget(southCheckbox)

        moveDownButton = MDFlatButton(text='Mover abaixo', on_press=lambda _: self.addWaypoint('moveDown'))
        moveUpButton = MDFlatButton(text='Mover acima', on_press=lambda _: self.addWaypoint('moveUp'))
        walkButton = MDFlatButton(text='Andar', on_press=lambda _: self.addWaypoint('walk'))
        useRopeButton = MDFlatButton(text='Usar corda', on_press=self.addUseRopeWaypoint)
        useShovelButton = MDFlatButton(text='Usar pá', on_press=self.addUseShovelWaypoint)
        buttonsLayout.add_widget(walkButton)
        buttonsLayout.add_widget(moveDownButton)
        buttonsLayout.add_widget(moveUpButton)
        buttonsLayout.add_widget(useRopeButton)
        buttonsLayout.add_widget(useShovelButton)
        wrapperLayout.add_widget(anchorLayout)
        wrapperLayout.add_widget(buttonsLayout)
        self.add_widget(wrapperLayout)

    def onCheckDirection(self, direction, checked):
        if checked:
            self.selectedDirection = direction

    def on_row_press(self, _, instance_row):
        '''Called when a table row is clicked.'''
        pass

    def addWaypoint(self, waypointType):
        context = kivy.context.get_current_context()['game']
        coordinate = context.getCoordinate()
        cannotGetCoordinate = coordinate is None
        if cannotGetCoordinate:
            toast('Não foi possível obter a coordenada! Verifique se o minimapa do cliente está aberto.')
            return
        if waypointType == 'moveDown':
            if self.selectedDirection == 'north':
                waypointType = 'moveDown'
            elif self.selectedDirection == 'south':
                waypointType = 'moveDown'
            elif self.selectedDirection == 'east':
                waypointType = 'moveDown'
            elif self.selectedDirection == 'west':
                waypointType = 'moveDown'
        elif waypointType == 'moveUp':
            if self.selectedDirection == 'north':
                waypointType = 'moveUp'
            elif self.selectedDirection == 'south':
                waypointType = 'moveUp'
            elif self.selectedDirection == 'east':
                waypointType = 'moveUp'
            elif self.selectedDirection == 'west':
                waypointType = 'moveUp'
        waypointRow = ('', waypointType, coordinate[0], coordinate[1], coordinate[2], {})
        self.data_tables.add_row(waypointRow)
        waypoint = (waypointRow[0], waypointRow[1], [waypointRow[2], waypointRow[3], waypointRow[4]], waypointRow[5])
        context.addWaypoint(waypoint)

    def addUseRopeWaypoint(self, _):
        context = kivy.context.get_current_context()['game']
        coordinate = context.getCoordinate()
        waypointRow = ('', 'useRope', coordinate[0], coordinate[1], coordinate[2], {})
        self.data_tables.add_row(waypointRow)
        waypoint = ('', 'useRope', coordinate, {})
        context.addWaypoint(waypoint)

    def addUseShovelWaypoint(self, _):
        context = kivy.context.get_current_context()['game']
        coordinate = context.getCoordinate()
        if self.selectedDirection == 'north':
            coordinate[1] -= 1
        elif self.selectedDirection == 'south':
            coordinate[1] += 1
        elif self.selectedDirection == 'east':
            coordinate[0] += 1
        elif self.selectedDirection == 'west':
            coordinate[0] -= 1
        waypointRow = ('', 'useShovel', coordinate[0], coordinate[1], coordinate[2], {})
        self.data_tables.add_row(waypointRow)
        waypoint = ('', 'useShovel', coordinate, {})
        context.addWaypoint(waypoint)
