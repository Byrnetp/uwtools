set -ae
source $(dirname ${BASH_SOURCE[0]})/common.sh
ci_conda_activate
conda build recipe -c conda-forge --override-channels
cd notebooks
source install-deps
make test-nb
