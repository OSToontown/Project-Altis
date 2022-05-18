cd "../dependencies/astron/"

chmod +x darwin/astrond
darwin/astrond --loglevel info config/cluster-yaml.yml
