
### pkg_interface
```bash
act -j build_pkg_interface -P arm=humble/arm:latest \
    --pull=false \
    --bind --directory . 
```


### pkg_server
```bash
act -j build_pkg_server -P arm=gst_stream/arm:runtime \
    --pull=false \
    --bind --directory . \
    --volume $(pwd)/../pkg_interface:/etc/ros/rosdep/sources.list.d/
```

<!-- 
### parameters_manager_ex
```bash
act -j build_parameters_manager_ex -P arm=gst_stream/arm:runtime \
    --pull=false \
    --bind --directory . 
``` -->