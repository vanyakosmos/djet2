require('jquery.cookie');

const $ = require('jquery');

const Themes = function () {
};

Themes.prototype = {
    moveChooser: function($chooser) {
        $chooser
            .detach()
            .insertAfter($('.user-tools-welcome-msg'))
            .addClass('initialized');
    },
    initChooser: function($chooser) {
        const $links = $chooser.find('.choose-theme');

        $links.on('click', function (e) {
            e.preventDefault();

            const $link = $(this);

            $.cookie('JET_THEME', $link.data('theme'), { expires: 365, path: '/' });

            const cssToLoad = [
                {url: $link.data('base-stylesheet'), class: 'base-stylesheet'},
                {url: $link.data('select2-stylesheet'), class: 'select2-stylesheet'},
                {url: $link.data('jquery-ui-stylesheet'), class: 'jquery-ui-stylesheet'}
            ];

            let loadedCss = 0;

            const onCssLoaded = function () {
                ++loadedCss;

                if (loadedCss === cssToLoad.length) {
                    $(document).trigger('theme:changed');
                }
            };

            $.each(cssToLoad, function() {
                $('<link>')
                    .attr('rel', 'stylesheet')
                    .addClass(this['class'])
                    .attr('href', this['url'])
                    .ready(onCssLoaded)
                    .appendTo('head');
                $('.' + this['class'])
                    .slice(0, -2)
                    .remove();
            });

            $links.removeClass('selected');
            $link.addClass('selected');
        });
    },
    run: function() {
        const $chooser = $('.theme-chooser');

        try {
            this.moveChooser($chooser);
            this.initChooser($chooser);
        } catch (e) {
            console.error(e, e.stack);
        }
    }
};

$(document).ready(function() {
    new Themes().run();
});
