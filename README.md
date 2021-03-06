# Transom

## Setup your environment

To setup paths in your environment, source the `config.sh` script.

    ~$ cd transom/
    transom$ . config.sh

## Project layout

    config.sh             # Sets up your project environment
    Makefile              # Defines the make targets
    python/               # Python library code; used by scripts
    scripts/              # Scripts called by the make rules
    input/                # The site content before rendering
    docs/                 # The rendered result

Some notable files in `input/`:

    input/template.html   # The standard page template
    input/site.js         # Site javascript code
    input/site.css        # Site CSS
    input/site.conf       # Site variables, values for @placeholders@

## Make targets

After that most everything is accomplished by running make targets.
These are the important ones:

    transom$ make render  # Renders input/* to docs/
    transom$ make clean   # Removes docs/

## Adding content

1. Use your editor to create or edit a file under `input/`

        transom$ emacs input/somepage.md

2. Render the site

        transom$ make render

3. To look at the result in your browser, navigate to 

        file:///$somepath/transom/docs/somepage.html

## Render transformations

The render step takes files under `input/` and reproduces them under
`docs/`.  The following transformations are applied in the process:

 - `.html` files are just copied
 - `.html.in` files are wrapped in the site template and copied
 - `.md` (markdown) files are converted to HTML and then treated
   just as `.html.in` files are
 - All pages undergo substitution for `@placeholders@`

## Markdown syntax

Markdown is a markup language inspired by plain text conventions.
This page is written in markdown.  See this [syntax guide][syntax].

I personally benefit from using [emacs markdown mode][emacs].

[syntax]: http://daringfireball.net/projects/markdown/syntax 
[emacs]:  http://jblevins.org/projects/markdown-mode/

## Placeholders

`input/site.conf` defines some variables usable for any input page.
To illustrate:

    @site-url@                 -> http://qpid.apache.org
    @current-release@          -> 0.20
    @current-proton-release@   -> 0.4

You can see more definitions in `input/site.conf`.

## Generating release content

Most of the site content is written by human beings.  Release content,
however, is automated.  Use the following commands to generate content
for a new release.

    # For new Qpid releases
    transom$ make gen-release RELEASE=$VERSION
    
    # For new Qpid Proton releases    
    transom$ make gen-proton-release RELEASE=$VERSION
    
These will produce a new tree of release content under
`input/releases/`.  The content includes API docs, examples, and
books.  Once generated, you can make any edits you'd like and check it
in.

When you add release content, you should also update the following
files.

    input/site.conf            # Update the current release pointer
    input/releases/index.md    # Add current release, move the previous

The scripts depend on the availability of the following tools in your
environment: cmake, dot, doxygen, epydoc, gcc, javadoc, make,
pygments, rdoc, and xsltproc.  The following yum command works to
install all the required dependencies on Fedora or RHEL.

    $ sudo yum install cmake doxygen epydoc graphviz java-devel make python-pigments rubygem-rdoc libxslt

## Publishing your work

Once you're done making changes, commit your work.  All changes
committed under `docs/` will be automatically propagated to the live
Qpid website.
