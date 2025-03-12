## Cross compiler

```
colcon build --packages-select pkg_interface \
--cmake-args \
-DCMAKE_TOOLCHAIN_FILE=/home/user/workspaces/deploy_demo_ws/cmake/aarch64.cmake
```

## bloom

```
export ROSDISTRO_INDEX_URL=file:///home/user/workspaces/deploy_demo_ws/index-v4.yaml
bloom-generate rosdebian
fakeroot debian/rules binary

```

### Cross compiler

```bash
export DEB_BUILD_OPTIONS=nocheck
export DEB_CMAKE_EXTRA_FLAGS="-DCMAKE_TOOLCHAIN_FILE=/home/user/workspaces/deploy_demo_ws/cmake/aarch64.cmake"
bloom-generate rosdebian --os-name ubuntu --os-version jammy --ros-distro humble

```