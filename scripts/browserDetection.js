var BrowserDetection = {
    supportedBrowsers: [{
        browserName: "Chrome",
        minSupportedVersion: 48,
        upgradeLink: "https://www.google.com/chrome/"
    }, {
        browserName: "Firefox",
        minSupportedVersion: 38,
        upgradeLink: "https://support.mozilla.org/en-US/kb/update-firefox-latest-version"
    }, {
        browserName: "Opera",
        minSupportedVersion: 33,
        upgradeLink: "https://www.opera.com/"
    }, {
        browserName: "Safari",
        minSupportedVersion: 10,
        minMobileSupportedVersion: 0
    }, {
        browserName: "Chromium",
        minSupportedVersion: 69,
        upgradeLink: "https://www.chromium.org/getting-involved/download-chromium"
    }, {
        browserName: "Microsoft Edge",
        minSupportedVersion: 14.14291
    }, {
        browserName: "Googlebot",
        minSupportedVersion: 0
    }, {
        browserName: "Vivaldi",
        minSupportedVersion: 2
    }, {
        browserName: "Yandex Browser",
        minSupportedVersion: 18
    }],
    getBrowserName: function() {
        return bowser.name ? bowser.name : "Unknown"
    },
    getBrowserVersion: function() {
        return bowser.version ? parseFloat(bowser.version) : 0
    },
    getCurrentBrowserData: function() {
        for (var r = this.getBrowserName(), e = 0; e < this.supportedBrowsers.length; e += 1)
            if (this.supportedBrowsers[e].browserName === r) return this.supportedBrowsers[e]
    },
    isVersionSupported: function(r) {
        var e = this.getBrowserVersion();
        return !!r && (bowser.ios && void 0 !== r.minMobileSupportedVersion ? e >= r.minMobileSupportedVersion : e >= r.minSupportedVersion)
    },
    isBrowserUnsupported: function() {
        var r = this.getCurrentBrowserData();
        return !(r && this.isVersionSupported(r))
    },
    getUpgradeLink: function() {
        var r = this.getCurrentBrowserData();
        if (r) return r.upgradeLink
    }
};