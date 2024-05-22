import pandas as pd

class SocialData:
    data = {
        'world_bank.gdp_percentage': {
            'path': "/Users/jean.machado/projects/social_data_access/local_data/gdp_percentage/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_401130.csv",
        },
        'world_bank.gdp_absolute': {
            'path': "/Users/jean.machado/projects/social_data_access/local_data/gdp_absolute/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_401322.csv",
        }
    }

    def read(self, event_name: str) -> pd.DataFrame:
        if not event_name in self.data:
            raise ValueError(f"Event {event_name} does not exist")

        return pd.read_csv(self.data[event_name]['path'])