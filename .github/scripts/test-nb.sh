set -ae
source $(dirname ${BASH_SOURCE[0]})/common.sh
ci_conda_activate
source notebooks/install-deps
make test-nb
