"""
 Copyright 2014-2016 Red Hat, Inc.

 This file is part of Atomic App.

 Atomic App is free software: you can redistribute it and/or modify
 it under the terms of the GNU Lesser General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 Atomic App is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Lesser General Public License for more details.

 You should have received a copy of the GNU Lesser General Public License
 along with Atomic App. If not, see <http://www.gnu.org/licenses/>.
"""

"""
Update the below LABELS if ATOMICAPPVERSION & NULECULESPECVERSION are updated:
1) LABEL io.projectatomic.nulecule.atomicappversion in atomicapp Dockerfile
2) LABEL io.projectatomic.nulecule.specversion  in app Dockefile
"""

__ATOMICAPPVERSION__ = '0.6.1'
__NULECULESPECVERSION__ = '0.0.2'

EXTERNAL_APP_DIR = "external"
GLOBAL_CONF = "general"
APP_ENT_PATH = "application-entity"
CACHE_DIR = "/var/lib/atomicapp"

PARAMS_KEY = "params"
RESOURCE_KEY = "resource"
INHERIT_KEY = "inherit"
ARTIFACTS_KEY = "artifacts"
ARTIFACTS_FOLDER = "artifacts"
NAME_KEY = "name"
DEFAULTNAME_KEY = "default"
PROVIDER_KEY = "provider"
NAMESPACE_KEY = "namespace"
REQUIREMENTS_KEY = "requirements"

# Nulecule spec terminology vs the function within /providers
REQUIREMENT_FUNCTIONS = {
    "persistentVolume": "persistent_storage"
}

MAIN_FILE = "Nulecule"
ANSWERS_FILE = "answers.conf"
ANSWERS_RUNTIME_FILE = "answers.conf.gen"
ANSWERS_FILE_SAMPLE = "answers.conf.sample"
ANSWERS_FILE_SAMPLE_FORMAT = 'ini'
WORKDIR = ".workdir"

LOGGER_DEFAULT = "atomicapp"
LOGGER_COCKPIT = "cockpit"

HOST_DIR = "/host"

DEFAULT_PROVIDER = "kubernetes"
DEFAULT_CONTAINER_NAME = "atomic"
DEFAULT_NAMESPACE = "default"
DEFAULT_ANSWERS = {
    "general": {
        "namespace": DEFAULT_NAMESPACE
    }
}

PROVIDERS = ["docker", "kubernetes", "openshift", "marathon"]
PROVIDER_API_KEY = "provider-api"
PROVIDER_AUTH_KEY = "provider-auth"
PROVIDER_CONFIG_KEY = "provider-config"
PROVIDER_TLS_VERIFY_KEY = "provider-tlsverify"
PROVIDER_CA_KEY = "provider-cafile"

K8S_DEFAULT_API = "http://localhost:8080"

# Persistent Storage Formats
PERSISTENT_STORAGE_FORMAT = ["ReadWriteOnce", "ReadOnlyMany", "ReadWriteMany"]

# If running in an openshift POD via `oc new-app`, the ca file is here
OPENSHIFT_POD_CA_FILE = "/run/secrets/kubernetes.io/serviceaccount/ca.crt"

# Index
INDEX_IMAGE = "projectatomic/nulecule-library"
INDEX_DEFAULT_IMAGE_LOCATION = "localhost"
INDEX_NAME = "index.yaml"
INDEX_LOCATION = ".atomicapp/" + INDEX_NAME
INDEX_GEN_DEFAULT_OUTPUT_LOC = "./" + INDEX_NAME
