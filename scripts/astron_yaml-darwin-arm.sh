cd "../dependencies/astron/"

chmod +x darwin/astrond-arm
darwin/astrond-arm --loglevel info config/cluster-yaml.yml
