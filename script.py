from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

browser = webdriver.Firefox()

browser.get('https://staging4.tstprep.com/store/')

acceptBtn = WebDriverWait(browser, 8).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/aside/div/div/div[2]/button"))
)
acceptBtn.click()




# product2 = WebDriverWait(browser, 8).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "html body.bp-nouveau.page-template-default.page.page-id-124677.page-parent.theme-buddyboss-theme.et_divi_builder.woocommerce-shop.woocommerce-js.buddyboss-theme.bb-custom-typo.et-pb-theme-buddyboss.child.et-db.js.bb-page-loaded.gecko div#page.site div#content.site-content div.container div.bb-grid.site-content-grid div#primary.content-area.bb-grid-cell main#main.site-main article#post-124677.post-124677.page.type-page.status-publish.hentry div.entry-content div#et-boc.et-boc div#et_builder_outer_content.et_builder_outer_content div.et-l.et-l--post div.et_builder_inner_content.et_pb_gutters3 div.et_pb_with_border.et_pb_section.et_pb_section_1.content-section-wh.et_section_regular.et_section_transparent div.et_pb_row.et_pb_row_2.store-row4.det-store-row.et_pb_gutters2.et_pb_row_4col div.et_pb_column.et_pb_column_1_4.et_pb_column_3.et_clickable.et_pb_css_mix_blend_mode_passthrough div.et_pb_module.et_pb_image.et_pb_image_1.storebox-img"))
# )
# product2.click()



# product5 = WebDriverWait(browser, 8).until(    
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "html body.bp-nouveau.page-template-default.page.page-id-124677.page-parent.theme-buddyboss-theme.et_divi_builder.woocommerce-shop.woocommerce-js.buddyboss-theme.bb-custom-typo.et-pb-theme-buddyboss.child.et-db.js.bb-page-loaded.gecko div#page.site div#content.site-content div.container div.bb-grid.site-content-grid div#primary.content-area.bb-grid-cell main#main.site-main article#post-124677.post-124677.page.type-page.status-publish.hentry div.entry-content div#et-boc.et-boc div#et_builder_outer_content.et_builder_outer_content div.et-l.et-l--post div.et_builder_inner_content.et_pb_gutters3 div.et_pb_with_border.et_pb_section.et_pb_section_1.content-section-wh.et_section_regular.et_section_transparent div.et_pb_row.et_pb_row_4.store-row4.et_pb_gutters2.et_pb_row_4col div.et_pb_column.et_pb_column_1_4.et_pb_column_8.et_clickable.et_pb_css_mix_blend_mode_passthrough"))
# )
# product5.click()

time.sleep(10)


courses_for_duolingo = WebDriverWait(browser, 8).until(    
    EC.element_to_be_clickable((By.CSS_SELECTOR, "html body.bp-nouveau.page-template-default.page.page-id-124677.page-parent.theme-buddyboss-theme.et_divi_builder.woocommerce-shop.woocommerce-js.buddyboss-theme.bb-custom-typo.et-pb-theme-buddyboss.child.et-db.js.bb-page-loaded.gecko div#page.site div#content.site-content div.container div.bb-grid.site-content-grid div#primary.content-area.bb-grid-cell main#main.site-main article#post-124677.post-124677.page.type-page.status-publish.hentry div.entry-content div#et-boc.et-boc div#et_builder_outer_content.et_builder_outer_content div.et-l.et-l--post div.et_builder_inner_content.et_pb_gutters3 div.et_pb_with_border.et_pb_section.et_pb_section_1.content-section-wh.et_section_regular.et_section_transparent div.et_pb_row.et_pb_row_4.store-row4.et_pb_gutters2.et_pb_row_4col div.et_pb_column.et_pb_column_1_4.et_pb_column_8.et_clickable.et_pb_css_mix_blend_mode_passthrough"))
)

private_lessons_for_duolingo = WebDriverWait(browser, 8).until(    
    EC.element_to_be_clickable((By.CSS_SELECTOR, "html body.bp-nouveau.page-template-default.page.page-id-124677.page-parent.theme-buddyboss-theme.et_divi_builder.woocommerce-shop.woocommerce-js.buddyboss-theme.bb-custom-typo.et-pb-theme-buddyboss.child.et-db.js.bb-page-loaded.gecko div#page.site div#content.site-content div.container div.bb-grid.site-content-grid div#primary.content-area.bb-grid-cell main#main.site-main article#post-124677.post-124677.page.type-page.status-publish.hentry div.entry-content div#et-boc.et-boc div#et_builder_outer_content.et_builder_outer_content div.et-l.et-l--post div.et_builder_inner_content.et_pb_gutters3 div.et_pb_with_border.et_pb_section.et_pb_section_1.content-section-wh.et_section_regular.et_section_transparent div.et_pb_row.et_pb_row_4.store-row4.et_pb_gutters2.et_pb_row_4col div.et_pb_column.et_pb_column_1_4.et_pb_column_8.et_clickable.et_pb_css_mix_blend_mode_passthrough"))
)

score_evaluation_for_duolingo = WebDriverWait(browser, 8).until(    
    EC.element_to_be_clickable((By.CSS_SELECTOR, "html body.bp-nouveau.page-template-default.page.page-id-124677.page-parent.theme-buddyboss-theme.et_divi_builder.woocommerce-shop.woocommerce-js.buddyboss-theme.bb-custom-typo.et-pb-theme-buddyboss.child.et-db.js.bb-page-loaded.gecko div#page.site div#content.site-content div.container div.bb-grid.site-content-grid div#primary.content-area.bb-grid-cell main#main.site-main article#post-124677.post-124677.page.type-page.status-publish.hentry div.entry-content div#et-boc.et-boc div#et_builder_outer_content.et_builder_outer_content div.et-l.et-l--post div.et_builder_inner_content.et_pb_gutters3 div.et_pb_with_border.et_pb_section.et_pb_section_1.content-section-wh.et_section_regular.et_section_transparent div.et_pb_row.et_pb_row_4.store-row4.et_pb_gutters2.et_pb_row_4col div.et_pb_column.et_pb_column_1_4.et_pb_column_8.et_clickable.et_pb_css_mix_blend_mode_passthrough"))
)

complete_practice_test_pack = WebDriverWait(browser, 8).until(    
    EC.element_to_be_clickable((By.CSS_SELECTOR, "html body.bp-nouveau.page-template-default.page.page-id-124677.page-parent.theme-buddyboss-theme.et_divi_builder.woocommerce-shop.woocommerce-js.buddyboss-theme.bb-custom-typo.et-pb-theme-buddyboss.child.et-db.js.bb-page-loaded.gecko div#page.site div#content.site-content div.container div.bb-grid.site-content-grid div#primary.content-area.bb-grid-cell main#main.site-main article#post-124677.post-124677.page.type-page.status-publish.hentry div.entry-content div#et-boc.et-boc div#et_builder_outer_content.et_builder_outer_content div.et-l.et-l--post div.et_builder_inner_content.et_pb_gutters3 div.et_pb_with_border.et_pb_section.et_pb_section_1.content-section-wh.et_section_regular.et_section_transparent div.et_pb_row.et_pb_row_4.store-row4.et_pb_gutters2.et_pb_row_4col div.et_pb_column.et_pb_column_1_4.et_pb_column_8.et_clickable.et_pb_css_mix_blend_mode_passthrough"))
)

emergency_course = WebDriverWait(browser, 8).until(    
    EC.element_to_be_clickable((By.CSS_SELECTOR, "html body.bp-nouveau.page-template-default.page.page-id-124677.page-parent.theme-buddyboss-theme.et_divi_builder.woocommerce-shop.woocommerce-js.buddyboss-theme.bb-custom-typo.et-pb-theme-buddyboss.child.et-db.js.bb-page-loaded.gecko div#page.site div#content.site-content div.container div.bb-grid.site-content-grid div#primary.content-area.bb-grid-cell main#main.site-main article#post-124677.post-124677.page.type-page.status-publish.hentry div.entry-content div#et-boc.et-boc div#et_builder_outer_content.et_builder_outer_content div.et-l.et-l--post div.et_builder_inner_content.et_pb_gutters3 div.et_pb_with_border.et_pb_section.et_pb_section_1.content-section-wh.et_section_regular.et_section_transparent div.et_pb_row.et_pb_row_4.store-row4.et_pb_gutters2.et_pb_row_4col div.et_pb_column.et_pb_column_1_4.et_pb_column_8.et_clickable.et_pb_css_mix_blend_mode_passthrough"))
)

score_builder_program = WebDriverWait(browser, 8).until(    
    EC.element_to_be_clickable((By.CSS_SELECTOR, "html body.bp-nouveau.page-template-default.page.page-id-124677.page-parent.theme-buddyboss-theme.et_divi_builder.woocommerce-shop.woocommerce-js.buddyboss-theme.bb-custom-typo.et-pb-theme-buddyboss.child.et-db.js.bb-page-loaded.gecko div#page.site div#content.site-content div.container div.bb-grid.site-content-grid div#primary.content-area.bb-grid-cell main#main.site-main article#post-124677.post-124677.page.type-page.status-publish.hentry div.entry-content div#et-boc.et-boc div#et_builder_outer_content.et_builder_outer_content div.et-l.et-l--post div.et_builder_inner_content.et_pb_gutters3 div.et_pb_with_border.et_pb_section.et_pb_section_1.content-section-wh.et_section_regular.et_section_transparent div.et_pb_row.et_pb_row_4.store-row4.et_pb_gutters2.et_pb_row_4col div.et_pb_column.et_pb_column_1_4.et_pb_column_8.et_clickable.et_pb_css_mix_blend_mode_passthrough"))
)

private_lessons_1_4_sections = WebDriverWait(browser, 8).until(    
    EC.element_to_be_clickable((By.CSS_SELECTOR, "html body.bp-nouveau.page-template-default.page.page-id-124677.page-parent.theme-buddyboss-theme.et_divi_builder.woocommerce-shop.woocommerce-js.buddyboss-theme.bb-custom-typo.et-pb-theme-buddyboss.child.et-db.js.bb-page-loaded.gecko div#page.site div#content.site-content div.container div.bb-grid.site-content-grid div#primary.content-area.bb-grid-cell main#main.site-main article#post-124677.post-124677.page.type-page.status-publish.hentry div.entry-content div#et-boc.et-boc div#et_builder_outer_content.et_builder_outer_content div.et-l.et-l--post div.et_builder_inner_content.et_pb_gutters3 div.et_pb_with_border.et_pb_section.et_pb_section_1.content-section-wh.et_section_regular.et_section_transparent div.et_pb_row.et_pb_row_4.store-row4.et_pb_gutters2.et_pb_row_4col div.et_pb_column.et_pb_column_1_4.et_pb_column_8.et_clickable.et_pb_css_mix_blend_mode_passthrough"))
)

trial_lesson = WebDriverWait(browser, 8).until(    
    EC.element_to_be_clickable((By.CSS_SELECTOR, "html body.bp-nouveau.page-template-default.page.page-id-124677.page-parent.theme-buddyboss-theme.et_divi_builder.woocommerce-shop.woocommerce-js.buddyboss-theme.bb-custom-typo.et-pb-theme-buddyboss.child.et-db.js.bb-page-loaded.gecko div#page.site div#content.site-content div.container div.bb-grid.site-content-grid div#primary.content-area.bb-grid-cell main#main.site-main article#post-124677.post-124677.page.type-page.status-publish.hentry div.entry-content div#et-boc.et-boc div#et_builder_outer_content.et_builder_outer_content div.et-l.et-l--post div.et_builder_inner_content.et_pb_gutters3 div.et_pb_with_border.et_pb_section.et_pb_section_1.content-section-wh.et_section_regular.et_section_transparent div.et_pb_row.et_pb_row_4.store-row4.et_pb_gutters2.et_pb_row_4col div.et_pb_column.et_pb_column_1_4.et_pb_column_8.et_clickable.et_pb_css_mix_blend_mode_passthrough"))
)

speaking_evaluation = WebDriverWait(browser, 8).until(    
    EC.element_to_be_clickable((By.CSS_SELECTOR, "html body.bp-nouveau.page-template-default.page.page-id-124677.page-parent.theme-buddyboss-theme.et_divi_builder.woocommerce-shop.woocommerce-js.buddyboss-theme.bb-custom-typo.et-pb-theme-buddyboss.child.et-db.js.bb-page-loaded.gecko div#page.site div#content.site-content div.container div.bb-grid.site-content-grid div#primary.content-area.bb-grid-cell main#main.site-main article#post-124677.post-124677.page.type-page.status-publish.hentry div.entry-content div#et-boc.et-boc div#et_builder_outer_content.et_builder_outer_content div.et-l.et-l--post div.et_builder_inner_content.et_pb_gutters3 div.et_pb_with_border.et_pb_section.et_pb_section_1.content-section-wh.et_section_regular.et_section_transparent div.et_pb_row.et_pb_row_4.store-row4.et_pb_gutters2.et_pb_row_4col div.et_pb_column.et_pb_column_1_4.et_pb_column_8.et_clickable.et_pb_css_mix_blend_mode_passthrough"))
)

writing_essay_evaluations = WebDriverWait(browser, 8).until(    
    EC.element_to_be_clickable((By.CSS_SELECTOR, "html body.bp-nouveau.page-template-default.page.page-id-124677.page-parent.theme-buddyboss-theme.et_divi_builder.woocommerce-shop.woocommerce-js.buddyboss-theme.bb-custom-typo.et-pb-theme-buddyboss.child.et-db.js.bb-page-loaded.gecko div#page.site div#content.site-content div.container div.bb-grid.site-content-grid div#primary.content-area.bb-grid-cell main#main.site-main article#post-124677.post-124677.page.type-page.status-publish.hentry div.entry-content div#et-boc.et-boc div#et_builder_outer_content.et_builder_outer_content div.et-l.et-l--post div.et_builder_inner_content.et_pb_gutters3 div.et_pb_with_border.et_pb_section.et_pb_section_1.content-section-wh.et_section_regular.et_section_transparent div.et_pb_row.et_pb_row_4.store-row4.et_pb_gutters2.et_pb_row_4col div.et_pb_column.et_pb_column_1_4.et_pb_column_8.et_clickable.et_pb_css_mix_blend_mode_passthrough"))
)

reading_group_classes = WebDriverWait(browser, 8).until(    
    EC.element_to_be_clickable((By.CSS_SELECTOR, "html body.bp-nouveau.page-template-default.page.page-id-124677.page-parent.theme-buddyboss-theme.et_divi_builder.woocommerce-shop.woocommerce-js.buddyboss-theme.bb-custom-typo.et-pb-theme-buddyboss.child.et-db.js.bb-page-loaded.gecko div#page.site div#content.site-content div.container div.bb-grid.site-content-grid div#primary.content-area.bb-grid-cell main#main.site-main article#post-124677.post-124677.page.type-page.status-publish.hentry div.entry-content div#et-boc.et-boc div#et_builder_outer_content.et_builder_outer_content div.et-l.et-l--post div.et_builder_inner_content.et_pb_gutters3 div.et_pb_with_border.et_pb_section.et_pb_section_1.content-section-wh.et_section_regular.et_section_transparent div.et_pb_row.et_pb_row_4.store-row4.et_pb_gutters2.et_pb_row_4col div.et_pb_column.et_pb_column_1_4.et_pb_column_8.et_clickable.et_pb_css_mix_blend_mode_passthrough"))
)

listening_group_classes = WebDriverWait(browser, 8).until(    
    EC.element_to_be_clickable((By.CSS_SELECTOR, "html body.bp-nouveau.page-template-default.page.page-id-124677.page-parent.theme-buddyboss-theme.et_divi_builder.woocommerce-shop.woocommerce-js.buddyboss-theme.bb-custom-typo.et-pb-theme-buddyboss.child.et-db.js.bb-page-loaded.gecko div#page.site div#content.site-content div.container div.bb-grid.site-content-grid div#primary.content-area.bb-grid-cell main#main.site-main article#post-124677.post-124677.page.type-page.status-publish.hentry div.entry-content div#et-boc.et-boc div#et_builder_outer_content.et_builder_outer_content div.et-l.et-l--post div.et_builder_inner_content.et_pb_gutters3 div.et_pb_with_border.et_pb_section.et_pb_section_1.content-section-wh.et_section_regular.et_section_transparent div.et_pb_row.et_pb_row_4.store-row4.et_pb_gutters2.et_pb_row_4col div.et_pb_column.et_pb_column_1_4.et_pb_column_8.et_clickable.et_pb_css_mix_blend_mode_passthrough"))
)

speaking_group_classes = WebDriverWait(browser, 8).until(    
    EC.element_to_be_clickable((By.CSS_SELECTOR, "html body.bp-nouveau.page-template-default.page.page-id-124677.page-parent.theme-buddyboss-theme.et_divi_builder.woocommerce-shop.woocommerce-js.buddyboss-theme.bb-custom-typo.et-pb-theme-buddyboss.child.et-db.js.bb-page-loaded.gecko div#page.site div#content.site-content div.container div.bb-grid.site-content-grid div#primary.content-area.bb-grid-cell main#main.site-main article#post-124677.post-124677.page.type-page.status-publish.hentry div.entry-content div#et-boc.et-boc div#et_builder_outer_content.et_builder_outer_content div.et-l.et-l--post div.et_builder_inner_content.et_pb_gutters3 div.et_pb_with_border.et_pb_section.et_pb_section_1.content-section-wh.et_section_regular.et_section_transparent div.et_pb_row.et_pb_row_4.store-row4.et_pb_gutters2.et_pb_row_4col div.et_pb_column.et_pb_column_1_4.et_pb_column_8.et_clickable.et_pb_css_mix_blend_mode_passthrough"))
)

writing_group_classes = WebDriverWait(browser, 8).until(    
    EC.element_to_be_clickable((By.CSS_SELECTOR, "html body.bp-nouveau.page-template-default.page.page-id-124677.page-parent.theme-buddyboss-theme.et_divi_builder.woocommerce-shop.woocommerce-js.buddyboss-theme.bb-custom-typo.et-pb-theme-buddyboss.child.et-db.js.bb-page-loaded.gecko div#page.site div#content.site-content div.container div.bb-grid.site-content-grid div#primary.content-area.bb-grid-cell main#main.site-main article#post-124677.post-124677.page.type-page.status-publish.hentry div.entry-content div#et-boc.et-boc div#et_builder_outer_content.et_builder_outer_content div.et-l.et-l--post div.et_builder_inner_content.et_pb_gutters3 div.et_pb_with_border.et_pb_section.et_pb_section_1.content-section-wh.et_section_regular.et_section_transparent div.et_pb_row.et_pb_row_4.store-row4.et_pb_gutters2.et_pb_row_4col div.et_pb_column.et_pb_column_1_4.et_pb_column_8.et_clickable.et_pb_css_mix_blend_mode_passthrough"))
)

reading_practice_pack = WebDriverWait(browser, 8).until(    
    EC.element_to_be_clickable((By.CSS_SELECTOR, "html body.bp-nouveau.page-template-default.page.page-id-124677.page-parent.theme-buddyboss-theme.et_divi_builder.woocommerce-shop.woocommerce-js.buddyboss-theme.bb-custom-typo.et-pb-theme-buddyboss.child.et-db.js.bb-page-loaded.gecko div#page.site div#content.site-content div.container div.bb-grid.site-content-grid div#primary.content-area.bb-grid-cell main#main.site-main article#post-124677.post-124677.page.type-page.status-publish.hentry div.entry-content div#et-boc.et-boc div#et_builder_outer_content.et_builder_outer_content div.et-l.et-l--post div.et_builder_inner_content.et_pb_gutters3 div.et_pb_with_border.et_pb_section.et_pb_section_1.content-section-wh.et_section_regular.et_section_transparent div.et_pb_row.et_pb_row_4.store-row4.et_pb_gutters2.et_pb_row_4col div.et_pb_column.et_pb_column_1_4.et_pb_column_8.et_clickable.et_pb_css_mix_blend_mode_passthrough"))
)

listening_practice_pack = WebDriverWait(browser, 8).until(    
    EC.element_to_be_clickable((By.CSS_SELECTOR, "html body.bp-nouveau.page-template-default.page.page-id-124677.page-parent.theme-buddyboss-theme.et_divi_builder.woocommerce-shop.woocommerce-js.buddyboss-theme.bb-custom-typo.et-pb-theme-buddyboss.child.et-db.js.bb-page-loaded.gecko div#page.site div#content.site-content div.container div.bb-grid.site-content-grid div#primary.content-area.bb-grid-cell main#main.site-main article#post-124677.post-124677.page.type-page.status-publish.hentry div.entry-content div#et-boc.et-boc div#et_builder_outer_content.et_builder_outer_content div.et-l.et-l--post div.et_builder_inner_content.et_pb_gutters3 div.et_pb_with_border.et_pb_section.et_pb_section_1.content-section-wh.et_section_regular.et_section_transparent div.et_pb_row.et_pb_row_4.store-row4.et_pb_gutters2.et_pb_row_4col div.et_pb_column.et_pb_column_1_4.et_pb_column_8.et_clickable.et_pb_css_mix_blend_mode_passthrough"))
)

first_pricebox_btn = WebDriverWait(browser, 8).until(    
    EC.element_to_be_clickable((By.CSS_SELECTOR, "html body.bp-nouveau.page-template-default.page.page-id-124677.page-parent.theme-buddyboss-theme.et_divi_builder.woocommerce-shop.woocommerce-js.buddyboss-theme.bb-custom-typo.et-pb-theme-buddyboss.child.et-db.js.bb-page-loaded.gecko div#page.site div#content.site-content div.container div.bb-grid.site-content-grid div#primary.content-area.bb-grid-cell main#main.site-main article#post-124677.post-124677.page.type-page.status-publish.hentry div.entry-content div#et-boc.et-boc div#et_builder_outer_content.et_builder_outer_content div.et-l.et-l--post div.et_builder_inner_content.et_pb_gutters3 div.et_pb_with_border.et_pb_section.et_pb_section_1.content-section-wh.et_section_regular.et_section_transparent div.et_pb_row.et_pb_row_4.store-row4.et_pb_gutters2.et_pb_row_4col div.et_pb_column.et_pb_column_1_4.et_pb_column_8.et_clickable.et_pb_css_mix_blend_mode_passthrough"))
)