import subprocess
import logging
import sys

logging.basicConfig(
    filepath='/var/log/opencti-monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
services = [
    "minio" ,
    "elasticsearch" ,
    "rabbitmq-server" ,
    "mongod" ,
    "redis" ,
    "redis-server" ,
    "postgresql" ,
    "opencti-abuseip" ,
    "opencti-abuse-ssl" ,
    "opencti-alienvualt" ,
    "opencti-cisa" ,
    "opencti-crowdsec" ,
    "opencti-disarm-framework" ,
    "opencti-malpedia" ,
    "opencti-malwarebazaar" ,
    "opencti-mitre" ,
    "opencti-phishunt" ,
    "opencti" ,
    "opencti-urlhaus" ,
    "opencti-worker"
]

def is_active(service):
    result = subprocess.run(
        ["systemctl" , "is-active" , service],
        capture_output=True,
        text=True
    )
    return result.stdout.strip() == "active"

def restart_service(service):
    subprocess.run(
        ["systemctl" , "restart" , service],
        check=True
    )

def main():
    for service in services:
        status = is_active(service)
        if not status:
            logging.warning(f"service {service} is down. restarting...")
            restart_service(service)
            logging.info(f"service {service} restarted successfully.")
        else:
            logging.info(f"service {service} is running")
        
if __name__ == "__name__":
    main()