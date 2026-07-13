from .InformationGathering import InformationGathering



class SCAnning:

    @staticmethod
    def system_information():
        return {
            
            'functions':[
                InformationGathering.get_hostname,
                InformationGathering.get_os,
                InformationGathering.get_kernal,
                InformationGathering.get_cpu,
                InformationGathering.get_mountfile,
                InformationGathering.get_env,
                InformationGathering.get_path,
            ],'title':'System Information'
        }

    @staticmethod
    def user_information():
        return {
            
            'functions': [
                InformationGathering.get_id,
                InformationGathering.get_users,
                InformationGathering.get_groups,
                InformationGathering.get_guid,
                InformationGathering.get_existing_users_name,
                InformationGathering.get_existing_users_full,
                InformationGathering.get_login_shells,
            ],
            'title':'User information',
        }

    @staticmethod
    def file_permissions():
        return {
       
        'functions' :[
            InformationGathering.get_suid,
            InformationGathering.get_sticky_bit_check,
            InformationGathering.get_world_write_files,
            InformationGathering.get_world_write_folder,
            InformationGathering.get_shadow_permissions,
            InformationGathering.get_capabilites,
            ], 'title':'Files permisson ',
        }

    @staticmethod
    def hidden_files():
        return {
       
        'functions':[
            InformationGathering.get_all_hidden_files_stream,
            InformationGathering.get_all_hidden_dir_stream,
        ], 'title':'Hidden files',}

    @staticmethod
    def network_information():
        return {
       
        'functions':[
            InformationGathering.get_networks,
            InformationGathering.get_ssh,
            ], 'title':'Network configuration'
        }

    @staticmethod
    def scheduled_tasks():
        return {
        
        'functions':[
            InformationGathering.get_cron_daily,
        ],'title' : 'Scheduled tasks',}