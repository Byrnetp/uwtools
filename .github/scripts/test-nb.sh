set -ae
source $(dirname ${BASH_SOURCE[0]})/common.sh
ci_conda_activate
cd notebooks
source install-deps
ls
pwd
make test-nb
