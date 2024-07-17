set -ae
source $(dirname ${BASH_SOURCE[0]})/common.sh
ci_conda_activate
cd notebooks
source install-deps
make test-nb
