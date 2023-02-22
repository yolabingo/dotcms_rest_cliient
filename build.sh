#!/bin/bash
export DOTCMS_OPENAPI_GENERATED="$(pwd)/openapi_generated"
pushd /var/tmp
if [ ! -d openapi-generator ]
then
    git clone https://github.com/OpenAPITools/openapi-generator.git --depth 1
fi

cd openapi-generator

if [ ! -f modules/openapi-generator-cli/target/openapi-generator-cli.jar ]
then
    mvn clean package
fi

# fetch dotcms openapi spec
curl -o dotcms_openapi.yaml https://dotcms-qa-lts2301.dotcms.site/api/openapi.yaml

# generate python client
java -jar modules/openapi-generator-cli/target/openapi-generator-cli.jar \
    generate \
    --skip-validate-spec \
    -i  dotcms_openapi.yaml \
    -g python \
    --api-package dotcms_rest_client \
    --package-name dotcms_rest_client \
    -o $DOTCMS_OPENAPI_GENERATED
cd /var/tmp
# create python venv
python -m venv dotcms_openapi_generated
. dotcms_openapi_generated/bin/activate
pip install -U pip
pip install wheel
cd $DOTCMS_OPENAPI_GENERATED
python setup.py bdist_wheel
pip wheel --no-deps -w ../dist . && rm -rf build dist
deactivate
pushd
