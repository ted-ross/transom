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
    output/               # The rendered result

Some notable files in `input/`:

    input/template.html   # The standard page template
    input/site.js         # Site javascript code
    input/site.css        # Site CSS
    input/site.conf       # Site variables, values for @placeholders@

## Make targets

After that most everything is accomplished by running make targets.
These are the important ones:

    transom$ make render  # Renders input/* to output/
    transom$ make clean   # Removes output/

## Adding content

1. Use your editor to create or edit a file under `input/`

        transom$ emacs input/somepage.md

2. Render the site

        transom$ make render

3. To look at the result in your browser, navigate to 

        file:///$somepath/transom/output/somepage.html

## Render transformations

The render step takes files under `input/` and reproduces them under
`output/`.  The following transformations are applied in the process:

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

The scripts depend on the availability of the following tools in your
environment: dot, xsltproc, epydoc, rdoc, doxygen, and pygments.

## Publishing your work

Once you're done making changes, commit your work.  There are still a
few more steps, however, before the world can see it.

Qpid uses Subversion to update the public website from the content at
https://svn.apache.org/repos/asf/qpid/site/docs/. Any changes
committed there will be reflected on the Qpid website.

First make sure you have a local checkout of `qpid/site/docs`, then
run the following command.  For this example I'll assume
`qpid/site/docs` is checked out to `$HOME/qpid-site/docs`.

    transom$ make publish PUBLISH_DIR=$HOME/qpid-site/docs

This will copy your new content to the publish directory.  The final
step is to commit the changes there.

    transom$ cd $HOME/qpid-site/docs

    # Check that everything looks right; 'svn add' any new files
    docs$ svn status
    M       index.html
    ?       somenewfile.html

    # Last step! After this, the content is live
    docs$ svn checkin -m "Here I make an account of what I changed"
