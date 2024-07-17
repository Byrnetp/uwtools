set -ae
source $(dirname ${BASH_SOURCE[0]})/common.sh
source notebooks/install-deps
ci_conda_activate
make test-nb
