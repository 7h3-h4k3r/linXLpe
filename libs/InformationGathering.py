from . import subprocess , LPEAException


class InformationGathering:


    @staticmethod 
    def run_commend(commend,error_message):
        process = None
        collected_lines =[]
        try:
            process = subprocess.Popen(
                commend,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            for line in iter(process.stdout.readline, ''):
                clean_line = line.strip()
                if clean_line:
                    print(f" {clean_line}")
                    collected_lines.append(clean_line)
                    
                    
        except Exception as e:
            if process:
                process.kill()
            raise LPEAException(f"failed: {error_message}-{e}")
        
        finally:
            if process:
                if process.stdout:
                    process.stdout.close()
                if process.stderr:
                    process.stderr.close()
                
                process.wait()
        print(f"\n[+] Finished! Total files found: {len(collected_lines)}")
        
        return (True,collected_lines)
    
    @staticmethod
    def get_users():
        return (InformationGathering.run_commend(
            ['whoami'],
            'whoami command not found'
        ),'Current user and UID|GID')


    @staticmethod
    def get_groups():
        return (InformationGathering.run_commend(
            ['groups'],
            'groups command not found'
        ),'User groups')
            

    @staticmethod
    def get_id():
       return (InformationGathering.run_commend(
        ['id'],
        'id command not found'
       ),'identifier info')

    @staticmethod
    def get_hostname():
        return (InformationGathering.run_commend(
            ['hostname'],
            'hostname command not found'
        ),'Host information')
    
    @staticmethod
    def get_kernal():
        return (InformationGathering.run_commend(
            ['uname','-a'],
            'Uname command not found'
        ),'Kernal Version')

    
    @staticmethod
    def get_os():
        cmd ='cat /etc/os-release'
        return (InformationGathering.run_commend(
            cmd
            ,'Cat command not found'
        ),'Linux Distribution')
    

    @staticmethod
    def get_env():
        return (InformationGathering.run_commend(
            ['env'],
            'env command not found'
        ),'Environment variable Checking')
    


    @staticmethod
    def get_cpu():
        return (InformationGathering.run_commend(
            ['lscpu'],
            'lscpu tool not found'
        ),'Cpu information')
    
    @staticmethod
    def get_path():
        return (InformationGathering.run_commend(
            ['echo' ,'$PATH'],
            'path not exist '
        ),'Path variable configuration')

    @staticmethod
    def get_login_shells():
        return (InformationGathering.run_commend(
            ['cat''/etc/shells'],
            'cat commend not found'
        ),'valid login shells information')
    
    @staticmethod
    def get_existing_users_full():
        cmd = 'cat /etc/passwd'
        return (InformationGathering.run_commend(
            cmd,
            'cat commend not found'
        ),'Existing Users Lists')
    @staticmethod
    def get_existing_users_name():
        try:
            result = subprocess.run(
                ["cat", "/etc/passwd"],
                capture_output=True,
                text=True,
                check=True
            )

            users = "\n".join(
                line.split(":")[0]
                for line in result.stdout.splitlines()
                if line.strip()
            )

            return (users, "Existing Users List")

        except subprocess.CalledProcessError:
            return ("Failed to read /etc/passwd", "Existing Users List")

        except Exception as e:
            return (f"Error: {e}", "Existing Users List")
        
    @staticmethod
    def get_mountfile(unmount=False):
        str_val = 'Mounted file System'
        if unmount:
            with open('/etc/fstab', 'r') as f:
                lines = [line for line in f if not line.strip().startswith('#')]
            input_data = "".join(lines)
            result = subprocess.run(['column', '-t'], input=input_data, capture_output=True, text=True)
            return(result.stdout,'Un'+str_val)
        else:
            return (InformationGathering.run_commend(
                ['df','-h'],
                'df commend not found'
            ),str_val)

    @staticmethod
    def get_all_hidden_files_stream(user_name=None):
        user_name = InformationGathering.get_users()
        
        cmd = f'find / -type f -name ".*" -exec ls -l {{}} \\; 2>/dev/null | grep "{user_name}"'
        
        print(f"[*] Starting Hidden files scan for '{user_name}' hidden files...\n")
        
        return (InformationGathering.run_commend(
            cmd,
            'find commend not found'
            ),'All Hiddin files')
    
    @staticmethod
    def get_all_hidden_dir_stream():
        
        cmd = f'find / -type d -name ".*" -ls 2>/dev/null'

        print(f"[*] Starting Hidden  Directories scan")

        return (InformationGathering.run_commend(
            cmd,
            'find commend not found '
        ),'All Hidden Directoreies ')

    @staticmethod
    def get_sticky_bit_check():

        cmd = 'ls -l /tmp /var/tmp /dev/shm'

        print(f"[*] Starting Sticky bit scanning")

        return (InformationGathering.run_commend(
            cmd,
            ''
        ),'sticky bit checking')


    @staticmethod
    def get_shadow_permissions():

        cmd = 'ls -l /etc/passwd /etc/shadow'

        print(f"[*] Starting Sensitive file Permissions scaning")

        return (InformationGathering.run_commend(
            cmd,
            'ls not found'
        ),'Sensitive file Permissions')
    
    @staticmethod
    def get_networks():

        cmd = 'ip addr'

        print(f"[*] Starting network information scaning")

        result = InformationGathering.run_commend(
            cmd,
            'ip addr commend not found')
        

        
        cmd = 'ip route'
        result = InformationGathering.run_commend(
            cmd,
            'ip route commend not found'
        )

        if result:
            return (result,'Network scannign information\'s')


    @staticmethod  
    def get_suid():
        
        cmd  = 'find / -perm -4000 -type f 2>/dev/null'

        return (InformationGathering.run_commend(
            cmd,
            'find commend not found'
        ),'SUID Binaries')
    

    @staticmethod
    def get_guid():
        
        cmd = 'find / -type f -perm -2000 2>/dev/null'

        return (InformationGathering.run_commend(
            cmd,
            'commend not found'
        ),'SGID Binaries')


    @staticmethod
    def get_cron_daily():

        cmd = 'ls -la /etc/cron.daily'

        return (InformationGathering.run_commend(
            cmd,
            'error happening'
        ),'Checking for daily cron Jobs')
    

    @staticmethod
    def get_ssh():

        cmd = 'ls -l ~/.ssh'

        return (InformationGathering.run_commend(
            cmd,
            'ssh not found'
        ),'SSH keys for current user')

    @staticmethod
    def get_world_write_files():

        cmd = 'find / -path /proc -prune -o -type f -perm -o+w 2>/dev/null'

        return (InformationGathering.run_commend(
            cmd,
            'find not found '
        ),'Find world-writeable Files')
    

    @staticmethod
    def get_world_write_folder():

        cmd = 'find / -path /proc -prune -o -type d -perm -o+w 2>/dev/null'

        return (InformationGathering.run_commend(
            cmd,
            'find not found '
        ),'Find world-writeable Directoreies')


    @staticmethod
    def get_capabilites():

        cmd = 'find /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin -type f -exec getcap {} \;'

        return (InformationGathering.run_commend(
            cmd,
            'find not found'
        ),'Enumerating Capabilites')

