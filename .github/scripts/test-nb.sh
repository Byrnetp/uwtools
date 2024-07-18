set -ae
source $(dirname ${BASH_SOURCE[0]})/common.sh
ci_conda_activate
conda install --quiet --yes --repodata-fn repodata.json 
cd notebooks
source install-deps
make test-nb
