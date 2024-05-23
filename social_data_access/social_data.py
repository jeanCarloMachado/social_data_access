import pandas as pd
from social_data_access.config import DATA_METADATA

class SocialData:

    def read(self, event_name: str) -> pd.DataFrame:
        if not event_name in DATA_METADATA:
            raise ValueError(f"Event {event_name} does not exist")

        read_parameters = {}
        if 'read_parameters' in DATA_METADATA[event_name]:
            read_parameters = DATA_METADATA[event_name]['read_parameters']

        if DATA_METADATA[event_name]['path'].endswith('.xls') or DATA_METADATA[event_name]['path'].endswith('.xlsx'):
            return pd.read_excel(DATA_METADATA[event_name]['path'], **read_parameters)

        return pd.read_csv(DATA_METADATA[event_name]['path'], **read_parameters)