DTU Python support homepage
===========================

Welcome to the DTU Python support development site.

Our homepage is hosted [here](https://pythonsupport.dtu.dk).

If you are a DTU student and want help with installing
packages for a course at DTU, please visit
[pythonsupport.dtu.dk](https://pythonsupport.dtu.dk).



Building the documentation
--------------------------

To build the documentation in a controlled environment we recommend you
to use a virtual environment.
Subsequently, the required packages should be installed, and lastly the
documentation can be built.

The steps can be outlined like this:

1. Create a conda environment

       conda env create -f environment.yml
       conda activate ps-page-env
       npm install -g terminalizer

2. Render gifs

       make rendergifs
   
   This will render the terminal gifs for the website. The sphinx build will not fail if these gifs do not exist - but it will create error messages.

3. Build documentation

       make

   Now the documentation is build and can be found in `build/html`.

4. Open the documentation:

       firefox build/html/index.html

   And you should be ready to see the just build documentation.


Running Locally in Podman
-------------------------

You can easily run the site locally (and deployed) using containers. You'll need:
- `podman` (or `docker`)

Run the following:
```bash
podman build . --tag pythonsupport-page:dev
podman run --rm -it --cap-drop ALL --publish 3000:3000 pythonsupport-page:dev
```

To control things like cache headers, compression, healthcheck endpoint, and basic authentication, see the `static-web-server` environment variable reference: https://static-web-server.net/configuration/environment-variables/
