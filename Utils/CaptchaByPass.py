import pytest


class CaptchaByPass:
    @staticmethod
    def PassCaptcha(driver):
        cdp_script = """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
            
            for (const key of Object.keys(window)){
                if (key.includes('cdc_')){
                    delete window[key];
                }
            }
        """

        cdp_params = {
            "source": cdp_script
        }

        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", cdp_params)