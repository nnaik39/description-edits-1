// customize the experiment by specifying a view order and a trial structure
exp.customize = function() {
    // record current date and time in global_data
    this.global_data.startDate = Date();
    this.global_data.startTime = Date.now();
    // specify view order
    this.views_seq = [
        intro,
        botcaptcha,
        instruction_screen,
        main,
        postTest,
        thanks
    ];

    imageSeenBefore = [];
    health = [];

    main_trials = _.shuffle(main_trials)[0]

    console.log("Main trials ", main_trials)

    health.push(main_trials[0]);

    console.log("Health ", health)

    imageSeenBefore.push(health[0]['filename']);

    console.log("Image seen before ", imageSeenBefore)

    for (let i = 0; i < main_trials.length; i++) {
        if (!imageSeenBefore.includes(main_trials[i]['filename'])) {
            health.push(main_trials[i])

            imageSeenBefore.push(main_trials[i]['filename']);
        }
    }

    health = _.sampleSize(health, 6);
    // Randomly sample 6 of these

    console.log("Health ", health)

    main_trials.length = 0
    main_trials.push(...health)

    // randomize main trial order, but keep practice trial order fixed
    this.trial_info.main_trials = _.shuffle(main_trials);
    console.log("Number of stimuli");
    console.log(main_trials.length);
    console.log(this.trial_info.main_trials);

    // sample question order
    shopping = "Why did this image appear within this context?"
    travel = "You are browsing a <strong> travel website</strong>, with the goal of traveling to a new location."
    social_media = "You are browsing <strong> social media</strong>, with the goal of learning more about your connections."
    health = "You are browsing a <strong> health website</strong>, with the goal of learning how to live a healthier lifestyle."
    science_journals = "You are browsing <strong>science magazines</strong> (such as National Geographic), with the goal of learning more about recent science developments."
    news_journals = "You are browsing <strong>news websites</strong> (such as New York Times), with the goal of learning more about recent news developments."

    questions = _.shuffle([health, shopping, travel, social_media, science_journals, news_journals])
    // adds progress bars to the views listed
    // view's name is the same as object's name
    this.progress_bar_in = ["main"];
    // this.progress_bar_in = ['practice', 'main'];
    // styles: chunks, separate or default
    this.progress_bar_style = "default";
    // the width of the progress bar or a single chunk
    this.progress_bar_width = 100;
};