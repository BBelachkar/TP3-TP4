from dao.game_dao import GameDao
from dao.game_dao import PlayerDao
from dao.game_dao import VesselDao
from model.player import Player
from model.vessel import Vessel
from model.battlefield import Battlefield
from model.game import Game
class GameService:
    def __init__(self):
        self.game_dao = GameDao()
    def create_game(self, player_name: str, min_x: int, max_x: int, min_y: int,max_y: int, min_z: int, max_z: int) -> int:
        game = Game()
        battle_field = Battlefield(min_x, max_x, min_y, max_y, min_z, max_z)
        game.add_player(Player(player_name, battle_field))
        return self.game_dao.create_game(game)
    def join_game(self, game_id: int, player_name: str) -> bool:
        #find game using gameDAO
        self.game = GameDao.find_game(game_id)
        # we have to add the player to the game but we need the battlefield attribut in order to define the player
        
        self.game.add_player(Player(player_name),Battlefield = None)
        return True
    def get_game(self, game_id: int) -> Game:
        game = GameDao.find_game(game_id)
        
        return game
        
    def add_vessel(self, game_id: int, player_name: str, vessel_type: str,x: int, y: int, z: int) -> bool:
        game = self.get_game(game_id)
        #getting the player of the
        player = [p for p in game.get_players if p.name == player_name][0]
        battle_field = player.get_battlefield()
        #find the vessel by type assuming that it exists in the database using the VesselDao.find_vessel method
        vessel = VesselDao.find_vessel(type)
        battle_field.add_vessel(vessel)

    def shoot_at(self, game_id: int, shooter_name: str, vessel_id: int, x: int,y: int, z: int) -> bool:
        game = self.get_game(game_id)
        #getting the player of the
        player = [p for p in game.get_players if p.name == shooter_name][0]
        battle_field = player.get_battlefield()
        vessel = VesselDao.find_vessel_by_id(vessel_id)
        try:
            vessel.fire_at(x,y,z)
            return True
        except: 
            return False

    def get_game_status(self, game_id: int, shooter_name: str) -> str:
        game = self.get_game()
        player = [p for p in game.get_players if p.name == shooter_name][0]
        battle_field = player.get_battlefield()
        #am stuck here
        
