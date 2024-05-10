import configparser

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read
        self.read_ini_file()
    
    def read_ini_file(self):
        self.config.read('./config.ini')
                
        self.config_mouse = self.config['Mouse']               
        self.screen_width = int(self.config_mouse['screen_width'])
        self.screen_height = int(self.config_mouse['screen_height'])
        self.fov_x = int(self.config_mouse['fov_x'])
        self.fov_y = int(self.config_mouse['fov_y'])
        self.mouse_dpi = int(self.config_mouse['mouse_dpi'])
        self.mouse_sensitivity = float(self.config_mouse['mouse_sensitivity'])
        
        self.config_generation = self.config['Generation']
        self.delete_prev_data = self.config.getboolean('Generation','delete_prev_data')
        self.generate_data = self.config.getboolean('Generation','generate_data')
        self.gen_time = int(self.config_generation['gen_time'])
        self.gen_visualise = self.config.getboolean('Generation','gen_visualise')
        self.gen_visualise_draw_line = self.config.getboolean('Generation','gen_visualise_draw_line')

        self.config_training = self.config['Training']
        self.train = self.config.getboolean('Training','train')
        self.train_epochs = int(self.config_training['train_epochs'])
        self.train_batch_size = int(self.config_training['train_batch_size'])
        self.save_every_N_epoch = int(self.config_training['save_every_N_epoch'])
        self.learning_rate = float(self.config_training['learning_rate'])
        
        self.config_speed = self.config['Speed']
        self.gen_speed_x = [int(x) for x in self.config_speed['gen_speed_x'].strip("[]").split(',')]
        self.gen_speed_y = [int(y) for y in self.config_speed['gen_speed_y'].strip("[]").split(',')]

        self.config_random = self.config['Random_game_settings']
        self.random_screen_resolution = self.config.getboolean('Random_game_settings','random_screen_resolution')
        
        self.random_screen_resolution_width = [int(x) for x in self.config_random['random_screen_resolution_width'].strip("[]").split(',')]
        self.random_screen_resolution_height = [int(x) for x in self.config_random['random_screen_resolution_height'].strip("[]").split(',')]
        
        self.random_fov = self.config.getboolean('Random_game_settings','random_fov')
        self.random_fov_x = [int(x) for x in self.config_random['random_fov_x'].strip("[]").split(',')]
        self.random_fov_y = [int(y) for y in self.config_random['random_fov_y'].strip("[]").split(',')]

        self.random_mouse_dpi = self.config.getboolean('Random_game_settings','random_mouse_dpi')
        self.random_mouse_dpi_min_max = [int(x) for x in self.config_random['random_mouse_dpi_min_max'].strip("[]").split(',')]

        self.random_mouse_sensitivity = self.config.getboolean('Random_game_settings','random_mouse_sensitivity')
        self.random_mouse_sensitivity_min_max = [float(x) for x in self.config_random['random_mouse_sensitivity_min_max'].strip("[]").split(',')]
        
        self.test_model = self.config.getboolean('Testing','test_model')
        
        
cfg = Config()
