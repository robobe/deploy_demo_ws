
!!! tip ""
    Run action from project root
     

### pkg_interface
```bash
act -j build_pkg_interface -P arm=humble/arm:latest \
    --pull=false \
    --bind --directory . 
```


### pkg_server
```bash
act -j build_pkg_server -P arm=humble/arm:latest \
    --pull=false \
    --bind --directory . 
```

### pkg_client
```bash
act -j build_pkg_client -P arm=humble/arm:latest \
    --pull=false \
    --bind --directory . 
```

### test
```bash
act -j test -P arm=humble/arm:dev \
    --pull=false \
    --userns=host \
    --privileged=false \
    --bind --directory . 
```