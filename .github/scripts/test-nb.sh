set -ae
source $(dirname ${BASH_SOURCE[0]})/common.sh
ci_conda_activate
cd notebooks
source install-deps
conda install -c ufs-community -c conda-forge --override-channels uwtools=2.3.2
make test-nb
