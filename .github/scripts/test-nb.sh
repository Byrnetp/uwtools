set -ae
source $(dirname ${BASH_SOURCE[0]})/common.sh
ci_conda_activate
conda install -c ufs-community -c conda-forge --override-channels uwtools
cd notebooks
source install-deps
make test-nb
