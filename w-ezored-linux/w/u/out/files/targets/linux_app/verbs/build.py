"""Build target"""

import os

from pygemstones.io import file as f
from pygemstones.system import runner as r
from pygemstones.type import list as ls
from pygemstones.util import log as l

from files.config import target_linux_app as config
from files.core import const


# -----------------------------------------------------------------------------
def run(params):
    proj_path = params["proj_path"]
    target_name = params["target_name"]
    target_config = config.run(proj_path, target_name, params)

    archs = target_config["archs"]
    build_types = target_config["build_types"]
    param_dry_run = ls.list_has_value(params["args"], "--dry-run")

    if param_dry_run:
        l.i("Running in dry mode...")

    if archs and len(archs) > 0:
        for arch in archs:
            for build_type in build_types:
                l.i("Building for: {0}/{1}...".format(arch["conan_arch"], build_type))

                # conan build
                build_dir = os.path.join(
                    proj_path,
                    const.DIR_NAME_BUILD,
                    target_name,
                    build_type,
                    arch["conan_arch"],
                    const.DIR_NAME_BUILD_TARGET,
                )

                clean_build_dir = True

                if param_dry_run and os.path.isdir(build_dir):
                    clean_build_dir = False

                if clean_build_dir:
                    f.recreate_dir(build_dir)

                run_args = [
                    "conan",
                    "build",
                    os.path.join(
                        proj_path,
                        const.DIR_NAME_FILES,
                        const.DIR_NAME_FILES_TARGETS,
                        target_name,
                        const.DIR_NAME_FILES_TARGET_CONAN,
                        const.DIR_NAME_FILES_TARGET_CONAN_RECIPE,
                        const.FILE_NAME_FILES_TARGET_CONAN_RECIPE_CONANFILE_PY,
                    ),
                    "--source-folder",
                    os.path.join(
                        proj_path,
                        const.DIR_NAME_FILES,
                        const.DIR_NAME_FILES_TARGETS,
                        target_name,
                        const.DIR_NAME_FILES_TARGET_CMAKE,
                    ),
                    "--build-folder",
                    os.path.join(
                        proj_path,
                        const.DIR_NAME_BUILD,
                        target_name,
                        build_type,
                        arch["conan_arch"],
                        const.DIR_NAME_BUILD_TARGET,
                    ),
                    "--install-folder",
                    os.path.join(
                        proj_path,
                        const.DIR_NAME_BUILD,
                        target_name,
                        build_type,
                        arch["conan_arch"],
                        const.DIR_NAME_BUILD_CONAN,
                    ),
                ]

                r.run(run_args, cwd=build_dir)

                # copy assets
                if "assets_dir" in target_config:
                    assets_dir = target_config["assets_dir"]

                    assets_dir = os.path.join(proj_path, assets_dir)

                    if os.path.isdir(assets_dir):
                        build_assets_dir = os.path.join(
                            build_dir, "bin", os.path.basename(assets_dir)
                        )

                        f.remove_dir(build_assets_dir)

                        f.copy_dir(assets_dir, build_assets_dir, symlinks=True)

        l.ok()
    else:
        l.error('Arch list for "{0}" is invalid or empty'.format(target_name))
