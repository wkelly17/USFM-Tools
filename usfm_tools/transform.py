import os
import logging
import pathlib
from usfm_tools.support import singlehtmlRenderer


logger = logging.getLogger("usfm_tools")


def buildSingleHtmlFromFile(
    filePath: pathlib.Path, builtDir: str, buildName: str
) -> None:
    """
    Given a file path, build the resulting HTML
    file named buildName and place it in builtDir.
    """

    logger.info("Building Single Page HTML...")
    ensureOutputDir(builtDir)
    c = singlehtmlRenderer.SingleHTMLRenderer(
        filePath, os.path.join(builtDir, "{}.html".format(buildName))
    )
    c.renderBody()


def ensureOutputDir(dir: str) -> None:
    if not os.path.exists(dir):
        os.makedirs(dir)
